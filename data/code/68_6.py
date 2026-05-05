import sys
if __name__ == '__main__':
    input_data = "10 20 30"
    parts = input_data.split()
    if len(parts) >= 2:
        first = int(parts[0])
        last = int(parts[-1])
        print(last - first)