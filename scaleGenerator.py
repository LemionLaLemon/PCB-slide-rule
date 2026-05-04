import math

# Settings
scale_length_mm = 80.0
total_decades = 2  # A-scale is two decades (1-10 and 10-100)
start_y = 0.0      # Y-coordinate for the base of the lines
layer = "F.SilkS"  # Front Silk Screen layer

def generate_log_scale():
    lines = []
    # Loop from 1 to 100
    for i in range(1, 101):
        # Calculate logarithmic position
        # x = total_length * log10(current_val) / log10(max_val)
        x_pos = scale_length_mm * math.log10(i) / math.log10(100)
        
        # Apply height logic
        if i == 1 or i % 10 == 0:
            height = 4.0  # 1, 10, 20, 30... 100
        elif i % 5 == 0:
            height = 2.0  # 5, 15, 25...
        else:
            height = 1.0  # All other marks
            
        lines.append({
            'start': (round(x_pos, 3), start_y),
            'end': (round(x_pos, 3), round(start_y - height, 3)),
            'val': i
        })
    return lines

# Generate and print in KiCad S-Expression format
scale_lines = generate_log_scale()
print(f";; Generated A-Scale Lines for KiCad")
for line in scale_lines:
    s, e = line['start'], line['end']
    print(f"(gr_line (start {s[0]} {s[1]}) (end {e[0]} {e[1]}) (stroke (width 0.15) (type solid)) (layer \"{layer}\"))")
