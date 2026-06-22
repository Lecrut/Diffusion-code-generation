def build_number_pyramid(levels):
    result = []
    current_number = 1
    row_width = 1
    total_rows = levels
    padding_spaces = (2 * levels - 1) // 2

    for i in range(levels):
        numbers_in_row = row_width
        row_numbers = [str(current_number + j) for j in range(numbers_in_row)]
        current_number += numbers_in_row
        
        row_str = " ".join(row_numbers)
        padding = " " * (padding_spaces - i)
        formatted_row = padding + row_str + padding
        result.append(formatted_row)
    
    return "\n".join(result)

if __name__ == "__main__":
    sample_levels = 4
    output = build_number_pyramid(sample_levels)
    print(output)