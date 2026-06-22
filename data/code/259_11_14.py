def find_min_max(data):
    return min(data), max(data)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    try:
        with open('input.txt', 'w') as f:
            for item in sample_list:
                f.write(f"{item}\n")
        
        with open('input.txt', 'r') as f:
            data = [int(line.strip()) for line in f.readlines()]
        
        minimum, maximum = find_min_max(data)
        
        with open('output.txt', 'w') as f:
            f.write(f"Minimum: {minimum}\n")
            f.write(f"Maximum: {maximum}\n")
    except FileNotFoundError:
        print("Error: input.txt not found.")
    except ValueError:
        print("Error: input.txt contains non-integer values.")