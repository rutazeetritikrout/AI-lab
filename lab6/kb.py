# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 14:14:48 2020

@author: rutaz
"""

def disjunctify(clauses):
    disjuncts = []
    for clause in clauses:
        disjuncts.append(tuple(clause.split('v')))
    return disjuncts
def getResolvant(ci, cj, di, dj):
    resolvant = list(ci) + list(cj)
    resolvant.remove(di)
    resolvant.remove(dj)
    return tuple(resolvant)
def resolve(ci, cj):
    for di in ci:
        for dj in cj:
            if di == '~' + dj or dj == '~' + di:
                return getResolvant(ci, cj, di, dj)
def checkResolution(clauses, query):
    clauses += [query if query.startswith('~') else '~' + query]
    proposition = '^'.join(['(' + clause + ')' for clause in clauses])
    print(f'Trying to prove {proposition} by contradiction....')
    
    clauses = disjunctify(clauses)
    resolved = False
    new = set()
    
    while not resolved:
        n = len(clauses)
        pairs = [(clauses[i], clauses[j]) for i in range(n) for j in range(i + 1, n)]
        for (ci, cj) in pairs:
            resolvant = resolve(ci, cj)
            if not resolvant:
                resolved = True
                break
            new = new.union(set(resolvents))
        if new.issubset(set(clauses)):
            break
        for clause in new:
            if clause not in clauses:
                clauses.append(clause)
        
    if resolved:
        print('Contradiction failed, Knowledge Base entails the query, proved by resolution')
    else:
        print("Contradiction succeeded, Knowledge Base doesn't entail the query, no empty set produced after resolution")
# Test 1
clauses = input('Enter the clauses (separated by whitespace): ').split()
query = input('Enter the query: ')
checkResolution(clauses, query)
# Test 2
clauses = input('Enter the clauses (separated by whitespace): ').split()
query = input('Enter the query: ')
checkResolution(clauses, query)   