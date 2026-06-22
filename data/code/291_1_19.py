def shorter_length(cm1, cm2):
    if cm1 < cm2:
        return f"{cm1} cm"
    else:
        return f"{cm2} cm"

if __name__ == '__main__':
    print(shorter_length(50, 75))
    print(shorter_length(100, 80))