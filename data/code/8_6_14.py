def split_csv(input_string):
    return [part.strip() for part in input_string.split(',') if part.strip()]

if __name__ == '__main__':
    result = split_csv("  hello , world , , foo ,  ")
    print(result)