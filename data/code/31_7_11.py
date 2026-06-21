def compute_square_areas(sides):
    return [side ** 2 for side in sides]

if __name__ == '__main__':
    side_lengths = [3, 4, 5, 6]
    result = compute_square_areas(side_lengths)
    print(result)