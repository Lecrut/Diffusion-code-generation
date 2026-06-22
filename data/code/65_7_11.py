def feet_to_inches(feet):
    return feet * 36

def main():
    samples = [1, 5.5, 100, 0, -2.5]
    for sample in samples:
        print(feet_to_inches(sample))

if __name__ == '__main__':
    main()