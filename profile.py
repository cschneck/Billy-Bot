# DESCRIPTION: Creates a general profile of the characters in Hamlet
# Created June 2, 2017 


# Stuff to do:
# Finish incorporating characters
# Parse the text instead of hard-coding the answer (more a test of concept right now)

import argparse

def info(name):
    # input: name
    # output: name, status, family, entrance, exit, cause of death, word count, average sentiment, most negative moment, most positive moment, killed by, first word, last word, longest speechOB

    # Hamlet
    if name == 'Hamlet':
        
        status = 'Prince Of Denmark'
        
        father = 'King of Denmark'
        mother = 'Gertrude'
        family = [father,mother]
        
        ent_act = 1
        ent_scene = 2
        entrance = [ent_act,ent_scene]

        ex_act = 5
        ex_scene = 2
        exit = [ex_act,ex_scene]

        cod = 'Poisoned by a sword in a duel with Laeretes'

        kills = 'quite a few people'

        killed_by = 'Claudius (poisoner) and Laeretes (dueler)'

        wrdcnt = 10

        first_wrd = 'A little more than kin, and less than kind!'

        last_wrd = 'The rest is silence'

        longest_speech = 'find this from fafsta file in future'

        avg_sent = 10
        
        most_neg = 10
        most_pos = 10

    profile = [name,status,family,entrance,exit,cod,wrdcnt,avg_sent,most_neg,most_pos,kills,killed_by,first_wrd,last_wrd,longest_speech]
    return profile

def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("char_name",help='the name of the character in hamlet you wish to profile',type=str)
    args = parser.parse_args()
    
    profile = info(args.char_name)
    
    char_name = args.char_name

    parents = profile[2]
    father = parents[0]
    mother = parents[1]

    ent = profile[3]

    ex = profile[4]

    cod = profile[5]


    print('The character ' + char_name + ', ' + status + 'is the son of ' + father + ' and ' + mother)
    print('He enters the play in Act '+ str(ent[0]) + ', Scene ' + str(ent[1]))
    print('He exits the play in Act ' + str(ex[0]) + ', Scene ' + str(ent[1]))
    

if __name__ == '__main__':
    Main()

