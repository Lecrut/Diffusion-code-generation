def main():
    # Hard-coded sample values to avoid interactive prompts
    volume_a = 50
    volume_b = 100
    
    if volume_a > volume_b:
        print(f"{volume_a} is greater than {volume_b}")
    elif volume_a < volume_b:
        print(f"{volume_a} is less than {volume_b}")
    else:
        print(f"{volume_a} is equal to {volume_b}")

if __name__ == '__main__':
    main()