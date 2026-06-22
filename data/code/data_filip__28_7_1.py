def rle_generator(data):
    if not data:
        return
    count = 1
    length = len(data)
    for i in range(1, length):
        if data[i] == data[i - 1]:
            count += 1
        else:
            yield data[i - 1], count
            count = 1
    yield data[length - 1], count

if __name__ == '__main__':
    sample_string = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    result = list(rle_generator(sample_string))
    print(result)
    encoded_parts = [f"{char}{count}" for char, count in result]
    print("".join(encoded_parts))