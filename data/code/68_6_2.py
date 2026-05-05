import sys
if __name__ == '__main__':
    input_data = "10 20 30"
    parts = input_data.split()
    if len(parts) >= 2:
        first_num = int(parts[0])
        last_num = int(parts[-1])
        difference = last_num - first_num
        print(difference)