import copy
from random import randint

story = (
        "One day my {} friend and I decided to go to the {} game in {}. " +
        "We really wanted to see the {} play the {}. " +
        "We get into the game and It was a lot of fun. " +
        "We ate some {} {} and drank some {}. " +
        "We had a great time! We plan to go ahead next year!"
)

word_dict = {
    'adjective': ['greed', 'abrasive', 'grubby', 'rich', 'harsh', 'tasty'],
    'city name': ['Chicago', 'New York', 'Charlotte', 'Indianapolic', 'Louisville', 'Denver'],
    'noun': ['people', 'map', 'music', 'dog', 'hamster', 'ball', 'hotdog', 'salad'],
    'action verb': ['run', 'fall', 'crawl', 'scurry', 'cry', 'watch', 'swim', 'jump', 'bounce'],
    'sports noun': ['ball', 'mit', 'puck', 'uniform', 'helmet', 'scoreboard', 'player'],
    'place': ['park', 'desert', 'forest', 'resturant', 'waterfall']
}


def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words) - 1
    index = randint(0, cnt)
    return local_dict[type].pop(index)


def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective', local_dict),
        get_word('sports noun', local_dict),
        get_word('city name', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('action verb', local_dict),
        get_word('noun', local_dict),
        get_word('place', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict)
    )


print("STORY 1: ")
print(create_story())

print("STORY 2: ")
print(create_story())
