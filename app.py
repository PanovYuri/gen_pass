import random
from settings import do_word, translate

dates = []
keywords = []

password = {
    'pass' : '',
    'phrase': [],
}

construction_of_date = ['число', 'месяц', 'год']

# Read dates from file
with open('dates.txt', 'r', encoding='utf-8') as f:
    dates = [dict((lambda x: {'date': x[0], 'desc': x[1].replace('\n', '')})(i.split(' - '))) for i in f.readlines() if i[0] != '#']

# Read keywords from file
with open('keywords.txt', 'r', encoding='utf-8') as f:
    keywords = [i.replace('\n', '') for i in f.readlines()]

# Generate text part
def generate_text(word):
    mini_word = translate(word[:3])
    password['pass'] += mini_word
    password['phrase'].append(word)

def set_random_date():
    date = random.choice(dates)
    num_date = date['date'].split('.')
    n_part_date = random.randint(0, len(num_date))
    
    password['pass'] += num_date[n_part_date]
    password['phrase'].append('{} из {}'
    .format(
        construction_of_date[n_part_date], 
        date['desc']))
    


generate_text(random.choice(keywords))
generate_text(random.choice(do_word))
generate_text(random.choice(keywords))    
set_random_date()
set_random_date()

print(password['pass'])
print(password['phrase'])

