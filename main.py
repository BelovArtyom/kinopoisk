"""Project "Kinopoisk"
Contributors: Artyom Belov: 100%

"""


def validatedinput(inp, insmth):
    # input which is within the included actors/movies
    while inp not in insmth:
        inp = input("Некорректный ввод, попробуйте ещё раз.")
    return inp


def actorinput():
    # input of two different actors from actorlist
    inp = validatedinput(input("Введите имя первого актёра"), actorlist)
    firstactor = inp
    while inp == firstactor:
        inp = validatedinput(input("Введите имя второго актёра"), actorlist)
        if inp == firstactor:
            print("Второй актёр не может быть таким же, как и первый.")
    return firstactor, inp


def movieinput():
    # input of two different movies from movielist
    inp = validatedinput(input("Введите имя первого фильма"), movielist)
    firstmovie = inp
    while inp == firstmovie:
        inp = validatedinput(input("Введите имя второго фильма"), movielist)
        if inp == firstmovie:
            print("Второй фильм не может быть таким же, как и первый.")
    return firstmovie, inp


movielist = list()
actorlist = set()

movies = dict()
actors = dict()

with open("input.txt", "r") as file:
    filelines = file.readlines()
    # adding movie entries
    for x in range(0, len(filelines)):
        movie = filelines[x].split(":")
        movieactors = movie[1].split(", ")
        movies.update({movie[0]: movieactors})

        movielist.append(movie[0])
        actorlist.union(set(movieactors))

# I have no idea
# print(movielist, "\n", actorlist)

# making actor movie sets
actorlist = list(actorlist)
for x in range(0, len(actorlist)):
    actors[actorlist[x]] = set()

# adding movies to actor movie sets
for x in range(0, len(movielist)):
    movieactors = movies[movielist[x]]
    for y in range(0, len(movieactors)):
        actors[movieactors[y]].union(set(movielist[x]))


# asking user for what they want
command = None
commandmovies = ["общактёр", "общфильм", "толькперв"]
commandactors = ["всефильм", "пересактёр", "толькперв"]

while command != "нет":
    command = validatedinput(input("Запрос по фильмам или актёрам? (фильмы/актёры"), ["фильмы", "актёры"])
    if command == "фильмы":
        command = validatedinput(input("Введите тип запроса (общактёр, общфильм, толькперв)"), commandmovies)

        if command == "общактёр":
            commovies = movieinput()
            print(set(movies[commovies[0]]).union(set(movies[commovies[1]])))

        elif command == "общфильм":
            commovies = movieinput()
            print(set(movies[commovies[0]]).intersection(set(movies[commovies[1]])))

        elif command == "толькперв":
            commovies == movieinput()
            print(set(movies[commovies[0]]).difference(set(movies[commovies[1]])))

    elif command == "актёры":
        command = validatedinput(input("Введите тип запроса (всефильм, пересактёр, толькперв)"), commandactors)

        if command == "всефильм":
            comactors = actorinput()
            print(set(actors[comactors[0]]).union(set(actors[comactors[1]])))

        elif command == "пересактёр":
            comactors = actorinput()
            print(set(actors[comactors[0]]).intersection(set(actors[comactors[1]])))

        elif command == "толькперв":
            comactors = actorinput()
            print(set(actors[comactors[0]]).difference(set(actors[comactors[1]])))

    command = validatedinput(input("Желаете продолжить? (да/нет)"), ["да", "нет"])
