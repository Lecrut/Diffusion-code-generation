def calculate_harmonic_mean(ratio1, ratio2, ratio3):
    total = 1 / ratio1[0] + 1 / ratio2[0] + 1 / ratio3[0]
    harmonic_mean = (ratio1[0] * ratio2[0] * ratio3[0]) / total
    return harmonic_mean

if __name__ == '__main__':
    sample_ratio1 = (4, 5)
    sample_ratio2 = (6, 7)
    sample_ratio3 = (8, 9)
    result = calculate_harmonic_mean(sample_ratio1, sample_ratio2, sample_ratio3)
    print(result)