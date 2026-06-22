def is_leap(year: int) -> bool:
    bit_y = year
    div_4 = (bit_y & 0xFFFFFFFC) == bit_y
    div_4 = (year >> 2) << 2 == year
    div_100 = (year >> 6) << 6 == year
    div_400 = (year >> 8) << 8 == year
    r4 = div_4
    r100 = div_100
    r400 = div_400
    leap = r4 & ~r100 | r400
    return leap

if __name__ == '__main__':
    y4 = is_leap(2024)
    y100 = is_leap(1900)
    y400 = is_leap(2000)
    y401 = is_leap(2004)
    print((y4, y100, y400, y401))