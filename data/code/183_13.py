if __name__ == '__main__':
    text = "Alice Bob\nCharlie David\nEve Frank"
    all_names = [name for line in text.split('\n') for name in line.split()]
    print(all_names)