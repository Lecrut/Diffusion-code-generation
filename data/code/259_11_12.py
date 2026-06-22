def find_min_max(data):
    return min(data), max(data)

if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
    try:
        with open('input.txt', 'w') as file:
            for item in sample_list:
                file.write(f"{item}\n")
        
        with open('input.txt', 'r') as file:
            data = [int(line.strip()) for line in file.readlines()]
            minimum, maximum = find_min_max(data)
        
        with open('output.txt', 'w') as file:
            file.write(f"Minimum: {minimum}\nMaximum: {maximum}")
        
    except Exception as e:
        print(f"An error occurred: {e}")