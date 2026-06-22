def create_symmetric_number_pyramid(levels=4):
    if levels <= 0:
        return []
    
    pyramid = []
    for i in range(1, levels + 1):
        spaces = " " * (levels - i)
        numbers = " ".join(str(j) for j in range(1, i + 1))
        line = spaces + numbers + spaces
        pyramid.append(line)
    
    return pyramid

if __name__ == '__main__':
    result = create_symmetric_number_pyramid(4)
    print(result)