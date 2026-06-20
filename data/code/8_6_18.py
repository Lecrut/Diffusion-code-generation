def split_and_clean(text):
    return [part.strip() for part in text.split(',') if part.strip()]

if __name__ == '__main__':
    result = split_and_clean(" apple, banana ,orange,, ,grape ")
    print(result)