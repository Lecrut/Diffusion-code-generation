import sys
if __name__ == '__main__':
    input_data = "10 20 30"
    parts = input_data.split()
    if len(parts) >= 2:
        first_number = int(parts[0])
        last_number = int(parts[-1])
        difference = last_number - first_number
        print(difference)