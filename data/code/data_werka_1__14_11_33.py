def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return f"{volume1} is greater than {volume2}"
    elif volume1 < volume2:
        return f"{volume1} is less than {volume2}"
    else:
        return f"{volume1} is equal to {volume2}"

if __name__ == '__main__':
    volume_a = 500
    volume_b = 300
    result = compare_volumes(volume_a, volume_b)
    print(result)