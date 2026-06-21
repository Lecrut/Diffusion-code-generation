def map_constants_to_words():
    return {
        "RED": "color",
        "SQUARE": "shape",
        "CIRCLE": "shape",
        "JANUARY": "month"
    }

if __name__ == '__main__':
    constant_map = map_constants_to_words()
    print(constant_map)