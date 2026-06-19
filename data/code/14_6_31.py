def compare_volumes(volume1, volume2):
    if volume1 > volume2:
        larger = volume1
        smaller = volume2
    else:
        larger = volume2
        smaller = volume1
    
    difference = abs(larger - smaller)
    
    return (larger, smaller, difference)

if __name__ == '__main__':
    sample_volume1 = 3.5
    sample_volume2 = 7.2
    result = compare_volumes(sample_volume1, sample_volume2)
    print(result)