def render_hollow_square(size: int) -> list[str]:
    if size <= 0:
        return []
    if size == 1:
        return ["#"]
    
    top_bottom = "#" * size
    middle = "#" + " " * (size - 2) + "#"
    
    result = [top_bottom]
    for _ in range(size - 2):
        result.append(middle)
    if size > 1:
        result.append(top_bottom)
        
    return result

if __name__ == '__main__':
    square = render_hollow_square(5)
    for row in square:
        print(row)