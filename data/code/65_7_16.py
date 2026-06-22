def feet_to_inches(feet):
    return feet * 36

def main():
    sample_feet_values = [1, 2.5, 0, 10, 100.123]
    for feet in sample_feet_values:
        inches = feet_to_inches(feet)
        print(f"{feet} feet is equal to {inches} inches")

if __name__ == '__main__':
    main()