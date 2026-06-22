def compare_lengths(cm1, cm2):
    return (cm1, "cm") if cm1 < cm2 else (cm2, "cm")

if __name__ == '__main__':
    print(compare_lengths(150, 200))
    print(compare_lengths(300, 250))