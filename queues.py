import tensorflow as tf
#q = tf.FIFOQueue(3,"float")
#init = q.enqueue_many(([0.,0.,0.],))
#sess = tf.Session()
#x = q.dequeue()
#y = x+1
#q_inc = q.enqueue([y])


#sess.run(q_inc)
#print sess.run(q)
random_number = tf.random_uniform(shape=())
q = tf.FIFOQueue(6, dtypes=[tf.float32])
enqueue_op = q.enqueue(random_number)
sess = tf.Session()
print sess.run(q.size()) # prints 0
def run():
 for i in range(5):
 # print 'hi'
  sess.run(enqueue_op)
  print sess.run(q.size())
  #print str(sess.run(q))

run()
#print sess.run(q.size()) 
sess.run(q.dequeue())
print sess.run(q.size()) 
