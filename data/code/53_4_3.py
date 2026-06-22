import itertools

def generate_reverse_number_triangle(height):
    def generate_row(row_number, width):
        return "".join(str(i) for i in range(row_number, width + row_number))
    
    total_numbers = (height * (height + 1)) // 2
    current_number = total_numbers
    
    for row in range(height, 0, -1):
        numbers_for_row = row
        row_content = []
        for _ in range(numbers_for_row):
            row_content.append(str(current_number))
            current_number -= 1
        row_str = " ".join(row_content)
        yield row_str

if __name__ == '__main__':
    height = 3
    for line in generate_reverse_number_triangle(height):
        print(line)