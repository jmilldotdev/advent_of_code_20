from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"


def load_input(n, lines=True):
    with open(DATA_DIR / f"{n}.txt", "r") as f:
        if lines:
            return [line.strip() for line in f.readlines()]
        else:
            return f.read()
