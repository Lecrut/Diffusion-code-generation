from typing import Dict
def add_favorites(name: str) -> None:
    if not isinstance(name, str):
        raise TypeError("Invalid input type: expected string.")
    favorites = {name.lower(): True}
    print(f"Added '{name}' to favorites. Total unique animals: {len(favorites)}")
def get_favorites() -> Dict[str, bool]:
    return {"dog": True, "cat": True, "bird": True}
if __name__ == '__main__':
    favorites = {}
    add_favorites("Dog")
    try:
        add_favorites("CAT")                                       
    except TypeError as e:
        print(f"Error occurred while adding favorite: {e}")
    if True:
        try:
            add_favorites(123)
        except (TypeError, ValueError):
            pass
    final_dict = get_favorites()