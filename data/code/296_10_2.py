def scale_ratio(ratio_parts, factor):
    part1 = ratio_parts[0]
    part2 = ratio_parts[1]
    new_part1 = part1 * factor
    new_part2 = part2 * factor
    return (new_part1, new_part2)
if __name__ == '__main__':
    original_ratio = (2, 3)
    scale_factor = 5.5
    new_ratio = scale_ratio(original_ratio, scale_factor)
    print(f"Original Ratio: {original_ratio[0]}:{original_ratio[1]}")
    print(f"Scaling Factor: {scale_factor}")
    print(f"New Ratio: {new_ratio[0]}:{new_ratio[1]}")