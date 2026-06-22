import argparse

def calculate_perimeter(side_lengths):
    return sum(side_lengths)
if __name__ == '__main__':
    samples = {'sample1': [3, 4, 5], 'sample2': [], 'sample3': [10, 20, 30, 40], 'sample4': [7]}
    for name, lengths in samples.items():
        perimeter = calculate_perimeter(lengths)
        print(f'Perimeter of {name}: {perimeter}')