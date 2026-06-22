def rle_chunks(text):
    if not text:
        return
    iterator = iter(text)
    try:
        current_char = next(iterator)
        count = 1
    except StopIteration:
        return
    for char in iterator:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                yield f'{count}{current_char}'
            else:
                yield current_char
            current_char = char
            count = 1
    if count > 1:
        yield f'{count}{current_char}'
    else:
        yield current_char

def main():
    text = 'aabcccccaaa'
    result = list(rle_chunks(text))
    print(result)
if __name__ == '__main__':
    main()