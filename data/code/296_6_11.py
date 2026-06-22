def harmonic_mean_of_ratios(ratio1, ratio2, ratio3):
    try:
        term1 = 1 / (ratio1[0] * ratio2[1] * ratio3[1])
        term2 = 1 / (ratio1[1] * ratio2[0] * ratio3[1])
        term3 = 1 / (ratio1[1] * ratio2[1] * ratio3[0])
        return 3 / (term1 + term2 + term3)
    except ZeroDivisionError:
        raise ValueError("Ratios must not contain zero in the denominator")

if __name__ == '__main__':
    sample_ratio1 = (2, 3)
    sample_ratio2 = (4, 5)
    sample_ratio3 = (6, 7)
    result = harmonic_mean_of_ratios(sample_ratio1, sample_ratio2, sample_ratio3)
    print(result)