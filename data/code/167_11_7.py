class StoreInfo:
    STORE_NAME = 'Central Market'
    STORE_AGE = 20

    @staticmethod
    def get_store_info():
        return {
            'store_name': StoreInfo.STORE_NAME,
            'store_age': StoreInfo.STORE_AGE
        }

if __name__ == '__main__':
    store_info = StoreInfo.get_store_info()
    print(store_info)