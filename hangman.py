import color


def hangman(word, attempts):
    status_str = "_" * len(word)
    for i in range(attempts, 0, -1):
        status_str = does_we_have(status_str, word, input())
        print(status_str)
        if "_" not in status_str:
            break
    if "_" not in status_str:
        color.green("u win")
    else:
        color.red("u lose")
    color.magenta(f"guested word is {word}")


def does_we_have(now, word, letter):
    for i in range(len(word)):
        if word[i] == letter:
            color.yellow("u guess")
            return now[0:i] + letter + now[i + 1:]
    color.ligth_red("u wrong")
    return now


print("guess a word")
word = input()
print("how much attempts")
attempts = 0
while True:
    try:
        attempts = int(input())
        assert len(word) <= attempts
        break
    except ValueError:
        color.red("it's not number ,try again")
    except AssertionError:
        color.red("too few attempts , try again")

hangman(word, attempts)
