import math
# modules can import other modules, these will be resolved in order as they are encountered

#data  = httpx.get("http://example.com")

print("near the top of the file")


def f(x):
    print("hello")
    return math.sin(x) ** 2 - math.cos(x)


print("near the bottom of the file, __name__=", __name__)


if __name__ == "__main__":
    print("module imported as main")
    # main()
