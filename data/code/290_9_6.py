class MassConverter:
    def pounds_to_ounces(self, pounds):
        return int(pounds * 16)

if __name__ == '__main__':
    converter = MassConverter()
    print(converter.pounds_to_ounces(5))
    print(converter.pounds_to_ounces(10))