def main():
    result = lambda s1: (lambda s2: f"{s1}{s2}")( "Hello", "World" )
    print(result)
if __name__ == '__main__':
    main()