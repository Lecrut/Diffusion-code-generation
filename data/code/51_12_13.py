def generate_number_pyramid(size: int) -> list[str]:
    if size < 1:
        return []
    
    center_width = 2 * size - 1
    pyramid = []
    
    for row in range(1, size + 1):
        number = row
        num_str = str(number)
        num_width = len(num_str)
        
        padding = (center_width - num_width) // 2
        
        row_str = (
            ' ' * padding +
            num_str +
            ' ' * (center_width - num_width - padding)
        )
        
        pyramid.append(row_str)
    
    return pyramid

if __name__ == '__main__':
    result = generate_number_pyramid(6)
    print(result)