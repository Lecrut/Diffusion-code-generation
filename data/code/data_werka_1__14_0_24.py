def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        return "The first volume is larger."
    elif volume1 < volume2:
        return "The second volume is larger."
    else:
        return "Both volumes are equal."

if __name__ == '__main__':
    v1 = 5.5
    v2 = 3.2
    result = compare_volumes(v1, v2)
    print(result)