def name: 
  for (var i = 0; i < count; i++) {
    
  }
  len(x)
  import React from 'react'
  import renderer from 'react-test-renderer'
  import { Provider } from 'react-redux'
  
  import store from 'src/store'
  import { FileName } from '../FileName'
  
  describe('<FileName />', () => {
    const defaultProps = {}
    const wrapper = renderer.create(
      <Provider store={store}>
       <FileName {...defaultProps} />
      </Provider>,
    )
  
    test('render', () => {
      expect(wrapper).toMatchSnapshot()
    })
  })
