import gc


def clear_cuda_cache() -> None:
	"""Czyści pamięć podręczną CUDA (PyTorch), jeśli jest dostępna."""
	try:
		import torch
	except ImportError:
		print("PyTorch nie jest zainstalowany.")
		return

	gc.collect()

	if not torch.cuda.is_available():
		print("CUDA nie jest dostępna na tym urządzeniu.")
		return

	torch.cuda.empty_cache()

	# Dodatkowe czyszczenie dla IPC (jeśli używane)
	if hasattr(torch.cuda, "ipc_collect"):
		torch.cuda.ipc_collect()

	print("Pamięć podręczna CUDA została wyczyszczona.")


if __name__ == "__main__":
	clear_cuda_cache()
