import pickle
from cube.utils import DblpEval
from config import *
from Cube import Cube
from cube.cube_construction import DblpCube


def rank(cube):
	tuples = []
	for i, authors in enumerate(cube.id_to_author):
		tuples.append((i, len(authors & cube.init_authors)))
	tuples.sort(key=lambda t: t[1], reverse=True)
	return [t[0] for t in tuples]


if __name__ == '__main__':
	with open('data/cube.pkl', 'rb') as f:
		cube = pickle.load(f)
	with open('cube/models/step3.pkl', 'rb') as f:
		dblp = pickle.load(f)

	cube.initial_state(args.test_file, args.low_limit, args.high_limit, args.debug)
	cells = rank(cube)
	for i in range(0, 1000, 20):
		print('num cells %d' % i)
		authors = cube.all_authors(cells[:i])
		test = DblpEval(dblp, authors, label_type=label_type, method='greedy')
		test.writeGraph()
		test.clusteringLINE()
