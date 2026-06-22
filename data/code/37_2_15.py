base_length = 12
perp_height = 7

calc_parallelogram = lambda b, h: b * h

if __name__ == '__main__':
    width = base_length
    altitude = perp_height
    computed_area = calc_parallelogram(width, altitude)
    print(computed_area)