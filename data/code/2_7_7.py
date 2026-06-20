import csv
import io

def scale_volumes(input_data, output_filename, factor):
    output_lines = []
    header_written = False
    for row in input_data:
        if not row:
            continue
        if not header_written:
            output_lines.append(row)
            header_written = True
        else:
            parts = row.strip().split(',')
            if len(parts) >= 2:
                try:
                    name = parts[0]
                    volume_str = parts[1]
                    original_volume = float(volume_str)
                    scaled_volume = original_volume * factor
                    output_lines.append(f"{name},{scaled_volume}")
                except ValueError:
                    output_lines.append(row)
            else:
                output_lines.append(row)
    
    with open(output_filename, 'w', newline='') as f:
        f.write('\n'.join(output_lines))

    return output_lines

if __name__ == '__main__':
    sample_csv_content = "item,volume\nApple,10\nBanana,20\nCherry,30"
    sample_lines = sample_csv_content.split('\n')
    scaled_results = scale_volumes(sample_lines, 'scaled_volumes.csv', 2.5)
    for line in scaled_results:
        print(line)