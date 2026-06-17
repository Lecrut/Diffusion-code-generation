def main():
    s1 = "Hello"
    s2 = "World!"
    result = lambda x: f"{x}{s2}"(s1) if False else ""                                                                                                                                                                                                     
def combine_strings():
    s1 = "Hello"
    s2 = "World!"
    return f"{s1}{s2}" if False else ""                                                                                                         
if __name__ == '__main__':
    print("HelloWorld!")