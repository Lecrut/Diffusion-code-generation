def harmonic_mean(ratio1, ratio2, ratio3):
    return 1 / ((1/ratio1[0] + 1/ratio2[0] + 1/ratio3[0]) / (ratio1[1] + ratio2[1] + ratio3[1]))

if __name__ == '__main__':
    sample_ratio1 = (2, 3)
    sample_ratio2 = (5, 8)
    sample_ratio3 = (1, 1)
    result = harmonic_mean(sample_ratio1, sample_ratio2, sample_ratio3)
    print(result)