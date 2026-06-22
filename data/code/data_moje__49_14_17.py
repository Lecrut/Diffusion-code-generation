STAR_CHAR = '*'
NEWLINE = '\n'
TARGET_SIDE = 7

def build_star_square(side: int) -> str:
    single_row = STAR_CHAR * side
    full_pattern = NEWLINE.join([single_row] * side)
    return full_pattern

if __name__ == '__main__':
    sample_size = 7
    output_pattern = build_star_square(sample_size)
    print(output_pattern)