def render_diamond(n: int) -> str:
    lines = []
    for i in range(1, n * 2):
        if i <= n:
            stars = 2 * i - 1
        else:
            stars = 2 * (n * 2 - i) - 1
        
        padding = n - (stars // 2 + 1 // (stars % 2 + 1))
        if stars % 2 == 0:
             padding = n - stars // 2
        else:
             padding = n - (stars + 1) // 2
             
        if padding < 0:
            padding = 0

        line = " " * padding + "* " * (stars // 2) + "*" if stars % 2 == 1 else "* " * (stars // 2)
        if i % 2 == 0:
             line = " " * padding + "* " * (stars // 2).strip().rstrip()
             line = " " * padding + "* " * (stars // 2)
             line = line.rstrip()
        else:
             line = " " * padding + "* " * (stars // 2) + "*"
             line = line.rstrip()
        
        lines.append(line)
    
    return "\n".join(lines)

def get_diamond_string():
    return render_diamond(3)

if __name__ == '__main__':
    print(get_diamond_string())