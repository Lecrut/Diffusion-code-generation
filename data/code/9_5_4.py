def trim_string_excess_whitespace(text):
    return " ".join(text.split())

if __name__ == "__main__":
    sample = "   This   is    a     string       with       excessive        whitespace         "
    result = trim_string_excess_whitespace(sample)
    print(result)