class ZerothIndexAccessor:
    STATIC_ARRAY = [100, 200, 300, 400, 500]

    @staticmethod
    def retrieve_zeroth(data):
        return data[0]

    @classmethod
    def get_static_zeroth(cls):
        return cls.retrieve_zeroth(cls.STATIC_ARRAY)

if __name__ == '__main__':
    result = ZerothIndexAccessor.get_static_zeroth()
    print(result)