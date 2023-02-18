

if __name__ == "__main__":
    pokemon = ('pikachu', 'charmander', 'bulbasaur')
    print(pokemon[1])
    value = ('pikachu', 'charmander', 'bulbasaur')
    starter1, starter2, starter3 = value  
    print(value)
    print(starter1)
    print(starter2)
    print(starter3)
    
    name_tup = ('zoe',)
    print(name_tup)
    print('i' in name_tup)
    
    i = 0
    for i in range(2, 11):
        print(i)

    tias = ('This is a simple string')
    print(tias)
    for letter in tias:
        print(letter)
    tia = ('this', 'is', 'a', 'simple', 'set')
    print(tia)
    for word in tia:
        print(word)