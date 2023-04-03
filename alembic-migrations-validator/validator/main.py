import argparse


def validate_migrations(*args):
    # TODO
    pass


def main():
    # TODO: decide on possible args
    parser = argparse.ArgumentParser()
    # parser.add_argument("filenames", nargs="*")
    args = parser.parse_args()

    validate_migrations(*args)


if __name__ == "__main__":
    main()
