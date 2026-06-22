def generate_number_pyramid(height: int) -> list[str]:
    if height <= 0:
        return []
    
    max_width = height * 2 - 1
    result = []
    
    for row in range(1, height + 1):
        numbers = list(range(1, row + 1))
        pattern = numbers + numbers[:-1][::-1]
        line = " ".join(map(str, pattern))
        padding = (max_width - len(line)) // 2
        result.append(" " * padding + line)
    
    return result

if __name__ == '__main__':
    sample_height = 5
    pyramid = generate_number_pyramid(sample_height)
    for line in pyramid:
        print(line)