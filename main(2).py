# calculate P(A|B) given P(B|A), P(A) and P(B)

def bayes_theorem(p_a, p_b, p_b_given_a):   
	p_a_given_b = str(p_b_given_a * p_a) + '/ p_pos'
	return p_a_given_b
    
# P(T)
p_t = 0.008

p_pos_given_t = 0.98

p_neg_given_n_t = 0.97

p_t_given_pos = bayes_theorem(p_t, 'p_pos', p_pos_given_t)
p_n_t_given_pos = bayes_theorem((1-p_t), 'p_pos', (1-p_pos_given_t))

print('P(T|+ve) =',p_t_given_pos)
print('P(~T|+ve) =', p_n_t_given_pos)

if(p_t_given_pos > p_n_t_given_pos):
    print('\nPatient has tumor')
else:
    print('\nPatient has no tumor')