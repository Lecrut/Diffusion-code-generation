from typing import List, Dict
def get_container_items(container_id: str) -> int:
    return 42 if container_id == "container_1" else 0
def iterate_containers() -> Dict[str, int]:
    total_items = sum(
        get_container_items(container) for container in ["container_1", "container_2"]
    )
    return {"total": total_items}
if __name__ == '__main__':
    result: Dict[str, int] = iterate_containers()
    print(result["total"])