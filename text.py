import pyfiglet, sys

A = "\033[2m" #Abu-abu
B = "\033[31m" #Merah
C = "\033[32m" #Hijau
D = "\033[33m" #Kuning
E = "\033[34m" #Biru
F = "\033[35m" #Ungu
G = "\033[36m" #Cyan
H = "\033[37m" #Putih
I = "\033[90m" #Abu-abu gelap
J = "\033[91m" #Merah cerah
K = "\033[92m" #Hijau cerah
L = "\033[93m" #Kuning cerah
M = "\033[94m" #Biru cerah
N = "\033[95m" #Ungu cerah
O = "\033[96m" #Cyan cerah
P = "\033[97m" #Putih cerah

def banner():
	print("""
    \033[1;33m___   _____ __           \033[0m  \033[34m+-----------------+
   \033[1;33m/   | / ___// /_____  _____\033[0m \033[41mCoded by BEC\033[0m
  \033[1;33m/ /| | \__ \/ __/ __ \/ ___/\033[0m \033[41mDeveloped in Python\033[0m
 \033[1;32m/ ___ |___/ / /_/ /_/ / /    \033[0m \033[41mVersion 1.0\033[0m
\033[1;32m/_/  |_/____/\__/\____/_/    \033[0m  \033[34m+-----------------+\033[0m
""")
banner()

try:
	teks = input("\033[1;33mMasukkan teks: ")

	if teks == "":
		print("Teksnya masukin brow")
		sys.exit()

	def daftarFont():
		print("""
\033[0;36m+---------------------+
\033[36m| \033[1;33m>>> \033[1;32mDaftar font \033[1;33m<<< \033[0;36m|
\033[36m+---------------------+\033[0m
1. 1943____
2. 3-d
3. 3x5
4. 4x4_offr
5. 5lineoblique
6. 5x7
7. 5x8
8. 64f1____
9. 6x10
10. 6x9
11. a_zooloo
12. acrobatic
13. advenger
14. alligator
15. alligator2
16. alphabet
17. aquaplan
18. arrows
19. asc_____
20. ascii___
21. assalt_m
22. asslt__m
23. atc_____
24. atc_gran
25. avatar
26. b_m__200
27. banner
28. banner3
29. banner3-D
30. banner4
31. barbwire
32. basic
33. battle_s
34. battlesh
35. baz__bil
36. beer_pub
37. bell
38. big
39. bigchief
40. binary
41. block
42. brite
43. briteb
44. britebi
45. britei
46. broadway
47. bubble
48. bubble__
49. bubble_b
50. bulbhead
51. c1______
52. c2______
53. c_ascii_
54. c_consen
55. calgphy2
56. caligraphy
57. catwalk
58. caus_in_
59. char1___
60. char2___
61. char3___
62. char4___
63. charact1
64. charact2
65. charact3
66. charact4
67. charact5
68. charact6
69. characte
70. charset_
71. chartr
72. chartri
73. chunky
74. clb6x10
75. clb8x10
76. clb8x8
77. cli8x8
78. clr4x6
79. clr5x10
80. clr5x6
81. clr5x8
82. clr6x10
83. clr6x6
84. clr6x8
85. clr7x10
86. clr7x8
87. clr8x10
88. clr8x8
89. coil_cop
90. coinstak
91. colossal
92. com_sen_
93. computer
94. contessa
95. contrast
96. convoy__
97. cosmic
98. cosmike
99. cour
100. courb
101. courbi
102. couri
103. crawford
104. cricket
105. cursive
106. cyberlarge
107. cybermedium
108. cybersmall
109. d_dragon
110. dcs_bfmo
111. decimal
112. deep_str
113. defleppard
114. demo_1__
115. demo_2__
116. demo_m__
117. devilish
118. diamond
119. digital
120. doh
121. doom
122. dotmatrix
123. double
124. drpepper
125. druid___
126. dwhistled
127. e__fist_
128. ebbs_1__
129. ebbs_2__
130. eca_____
131. eftichess
132. eftifont
133. eftipiti
134. eftirobot
135. eftitalic
136. eftiwall
137. eftiwater
138. epic
139. etcrvs__
140. f15_____
141. faces_of
142. fair_mea
143. fairligh
144. fantasy_
145. fbr12___
146. fbr1____
147. fbr2____
148. fbr_stri
149. fbr_tilt
150. fender
151. finalass
152. fireing_
153. flyn_sh
154. fourtops
155. fp1_____
156. fp2_____
157. fraktur
158. funky_dr
159. future_1
160. future_2
161. future_3
162. future_4
163. future_5
164. future_6
165. future_7
166. future_8
167. fuzzy
168. gauntlet
169. ghost_bo
170. goofy
171. gothic
172. gothic__
173. graceful
174. gradient
175. graffiti
176. grand_pr
177. greek
178. green_be
179. hades___
180. heavy_me
181. helv
182. helvb
183. helvbi
184. helvi
185. heroboti
186. hex
187. high_noo
188. hills___
189. hollywood
190. home_pak
191. house_of
192. hypa_bal
193. hyper___
194. inc_raw_
195. invita
196. isometric1
197. isometric2
198. isometric3
199. isometric4
200. italic
201. italics_
202. ivrit
203. jazmine
204. jerusalem
205. joust___
206. katakana
207. kban
208. kgames_i
209. kik_star
210. krak_out
211. larry3d
212. lazy_jon
213. lcd
214. lean
215. letter_w
216. letters
217. letterw3
218. lexible_
219. linux
220. lockergnome
221. mad_nurs
222. madrid
223. magic_ma
224. marquee
225. master_o
226. maxfour
227. mayhem_d
228. mcg_____
229. mig_ally
230. mike
231. mini
232. mirror
233. mnemonic
234. modern__
235. morse
236. moscow
237. mshebrew210
238. nancyj
239. nancyj-fancy
240. nancyj-underlined
241. new_asci
242. nfi1____
243. nipples
244. notie_ca
245. npn_____
246. ntgreek
247. nvscript
248. o8
249. octal
250. odel_lak
251. ogre
252. ok_beer_
253. os2
254. outrun__
255. p_s_h_m_
256. p_skateb
257. pacos_pe
258. panther_
259. pawn_ins
260. pawp
261. peaks
262. pebbles
263. pepper
264. phonix__
265. platoon2
266. platoon_
267. pod_____
268. poison
269. puffy
270. pyramid
271. r2-d2___
272. rad_____
273. rad_phan
274. radical_
275. rainbow_
276. rally_s2
277. rally_sp
278. rampage_
279. rastan__
280. raw_recu
281. rci_____
282. rectangles
283. relief
284. relief2
285. rev
286. ripper!_
287. road_rai
288. rockbox_
289. rok_____
290. roman
291. roman___
292. rot13
293. rounded
294. rowancap
295. rozzo
296. runic
297. runyc
298. sans
299. sansb
300. sansbi
301. sansi
302. sblood
303. sbook
304. sbookb
305. sbookbi
306. sbooki
307. script
308. script__
309. serifcap
310. shadow
311. shimrod
312. short
313. skate_ro
314. skateord
315. skateroc
316. sketch_s
317. slant
318. slide
319. slscript
320. sm______
321. small
322. smisome1
323. smkeyboard
324. smscript
325. smshadow
326. smslant
327. smtengwar
328. space_op
329. spc_demo
330. speed
331. stacey
332. stampatello
333. standard
334. star_war
335. starwars
336. stealth_
337. stellar
338. stencil1
339. stencil2
340. stop
341. straight
342. street_s
343. subteran
344. super_te
345. t__of_ap
346. tanja
347. tav1____
348. taxi____
349. tec1____
350. tec_7000
351. tecrvs__
352. tengwar
353. term
354. thick
355. thin
356. threepoint
357. ti_pan__
358. ticks
359. ticksslant
360. tiles
361. times
362. timesofl
363. tinker-toy
364. tomahawk
365. tombstone
366. top_duck
367. trashman
368. trek
369. triad_st
370. ts1_____
371. tsalagi
372. tsm_____
373. tsn_base
374. tty
375. ttyb
376. tubular
377. twin_cob
378. twopoint
379. type_set
380. ucf_fan_
381. ugalympi
382. unarmed_
383. univers
384. usa_____
385. usa_pq__
386. usaflag
387. utopia
388. utopiab
389. utopiabi
390. utopiai
391. vortron_
392. war_of_w
393. wavy
394. weird
395. whimsy
396. xbrite
397. xbriteb
398. xbritebi
399. xbritei
400. xchartr
401. xchartri
402. xcour
403. xcourb
404. xcourbi
405. xcouri
406. xhelv
407. xhelvb
408. xhelvbi
409. xhelvi
410. xsans
411. xsansb
412. xsansbi
413. xsansi
414. xsbook
415. xsbookb
416. xsbookbi
417. xsbooki
418. xtimes
419. xtty
420. xttyb
421. yie-ar__
422. yie_ar_k
423. z-pilot_
424. zig_zag_
425. zone7___""")
	daftarFont()
	pilih = input("\033[1;32mPilih font!\nSalin/paste namanya: \033[1;33m")

	if pilih == "":
		print("Fontnya apa lurd")
		sys.exit()

	warna = input("""
\033[0;36m+-----------------------------------+
\033[36m| \033[1;33m>>>>>>>>>> \033[1;32mPilih warna \033[1;33m<<<<<<<<<< \033[0;36m|
\033[36m+-----------------------------------+\033[0m
\033[36m| \033[1;31mA. \033[0;36m| \033[1;0mAbu-abu \033[0;36m| \033[1;31mI. \033[0;36m| \033[1;0mAbu-abu gelap \033[36m|
\033[36m| \033[1;31mB. \033[0;36m| \033[1;0mMerah   \033[0;36m| \033[1;31mJ. \033[0;36m| \033[1;0mMerah cerah   \033[36m|
\033[36m| \033[1;31mC. \033[0;36m| \033[1;0mHijau   \033[0;36m| \033[1;31mK. \033[0;36m| \033[1;0mHijau cerah   \033[36m|
\033[36m| \033[1;31mD. \033[0;36m| \033[1;0mKuning  \033[0;36m| \033[1;31mL. \033[0;36m| \033[1;0mkuning cerah  \033[36m|
\033[36m| \033[1;31mE. \033[0;36m| \033[1;0mBiru    \033[0;36m| \033[1;31mM. \033[0;36m| \033[1;0mBiru cerah    \033[36m|
\033[36m| \033[1;31mF. \033[0;36m| \033[1;0mUngu    \033[0;36m| \033[1;31mN. \033[0;36m| \033[1;0mUngu cerah    \033[36m|
\033[36m| \033[1;31mG. \033[0;36m| \033[1;0mCyan    \033[0;36m| \033[1;31mO. \033[0;36m| \033[1;0mCyan cerah    \033[36m|
\033[36m| \033[1;31mH. \033[0;36m| \033[1;0mPutih   \033[0;36m| \033[1;31mP. \033[0;36m| \033[1;0mPutih cerah   \033[36m|\033[0m
\033[36m+-----------------------------------+
\033[1;32mPilih warna? \033[1;33m[A/B/C/D/E/F/G/H/I/J/K/L/M/N/O/P] \033[0m""")

	fg = pyfiglet.figlet_format(teks, pilih)

	if warna == "A":
		print(A+fg)
	elif warna == "B":
		print(B+fg)
	elif warna == "C":
        	print(C+fg)
	elif warna == "D":
        	print(D+fg)
	elif warna == "E":
        	print(E+fg)
	elif warna == "F":
        	print(F+fg)
	elif warna == "G":
        	print(G+fg)
	elif warna == "H":
        	print(H+fg)
	elif warna == "I":
        	print(I+fg)
	elif warna == "J":
        	print(J+fg)
	elif warna == "K":
        	print(K+fg)
	elif warna == "L":
        	print(L+fg)
	elif warna == "M":
        	print(M+fg)
	elif warna == "N":
        	print(N+fg)
	elif warna == "O":
        	print(O+fg)
	elif warna == "P":
        	print(P+fg)
	else:
		print("Warna gk tersedia lurd!")
		sys.exit()

except KeyboardInterrupt:
	print("Thank you lurd!")
	sys.exit()

