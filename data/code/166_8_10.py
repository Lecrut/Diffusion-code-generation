def merge_unique_colors(colors1, colors2):
    if not isinstance(colors1, list) or not all((isinstance(color, str) for color in colors1)):
        raise ValueError('colors1 must be a list of strings')
    if not isinstance(colors2, list) or not all((isinstance(color, str) for color in colors2)):
        raise ValueError('colors2 must be a list of strings')
    unique_colors = set(colors1 + colors2)
    return list(unique_colors)
if __name__ == '__main__':
    sample_colors1 = ['red', 'blue', 'green']
    sample_colors2 = ['yellow', 'blue', 'purple']
    merged_colors = merge_unique_colors(sample_colors1, sample_colors2)
    print(merged_colors)