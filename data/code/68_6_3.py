import sys
if __name__ == '__main__':
    input_data = "10 20 30"
    lines = input_data.strip().split('\n')
    if len(lines) >= 2:
        line1 = lines[0].split()
        line2 = lines[1].split()
        if len(line1) >= 2 and len(line2) >= 2:
            first_num_line1 = int(line1[0])
            last_num_line1 = int(line1[-1])
            difference1 = last_num_line1 - first_num_line1
            first_num_line2 = int(line2[0])
            last_num_line2 = int(line2[-1])
            difference2 = last_num_line2 - first_num_line2
            print(difference1)
            print(difference2)
        else:
            pass
    else:
        pass