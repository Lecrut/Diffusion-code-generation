reverse_str = lambda s: ''.join(s[i] if i < len(s)//2 else None for i in range(len(s)))
if __name__ == '__main__':
    print(reverse_str("Hello"))