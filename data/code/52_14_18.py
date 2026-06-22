def generate_diamond(size):
    if size <= 0:
        return ""
    
    half = size // 2
    top_half = []
    
    for i in range(1, half + 1):
        stars = " " * (half - i + 1) + "* " * i
        top_half.append(stars.rstrip())
    
    bottom_half = list(reversed(top_half))
    
    if size % 2 == 0:
        middle = top_half[-1]
        full_diamond = top_half + [middle] + bottom_half
    else:
        full_diamond = top_half + bottom_half
        
    return "\n".join(full_diamond)

if __name__ == '__main__':
    print(generate_diamond(5))